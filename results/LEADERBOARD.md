# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 24, 6:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1288 windows, 34463 settled trades, 420 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 679 | 33.9 | 35.3 | $-569.22 | -8.4% | $430.78 | -1.7 | done | can't tell from luck |
| value_ev10 | 1656 | 38.5 | 39.2 | $-866.26 | -5.2% | $133.74 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3458 | 50.8 | 50.2 | $-1109.81 | -3.2% | $-109.81 | -1.9 | done | can't tell from luck |
| value_ev5 | 2503 | 40.4 | 41.1 | $-1333.95 | -5.3% | $-333.95 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 2887 | 49.4 | 49.4 | $-1377.94 | -4.8% | $-377.94 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 2887 | 50.6 | 51.0 | $-1615.21 | -5.6% | $-615.21 | -3.1 | done | losing for real |
| trend_filter | 2037 | 48.9 | 50.5 | $-1663.73 | -8.2% | $-663.73 | -3.8 | done | losing for real |
| momentum_15m_0.10pct | 3458 | 49.2 | 50.3 | $-2136.52 | -6.2% | $-1136.52 | -3.7 | done | losing for real |
| coinflip | 4966 | 50.0 | 50.1 | $-2261.84 | -4.6% | $-1261.84 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4966 | 50.5 | 51.4 | $-2788.93 | -5.6% | $-1788.93 | -4.1 | done | losing for real |
| always_up | 4966 | 47.9 | 49.3 | $-3642.01 | -7.3% | $-2642.01 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8252 | 48.0 | 48.8 | $-4897.91 |
| ETH | 8901 | 48.2 | 48.2 | $-4883.29 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
