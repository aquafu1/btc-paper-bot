# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 892 windows, 24616 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 462 | 35.7 | 34.9 | $-81.30 | -1.8% | $918.70 | -0.3 | done | can't tell from luck |
| value_ev10 | 1129 | 38.3 | 39.1 | $-599.52 | -5.3% | $400.48 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 2079 | 49.9 | 49.8 | $-936.48 | -4.5% | $63.52 | -2.1 | done | losing for real |
| reversal_15m_0.10pct | 2514 | 50.6 | 50.4 | $-976.12 | -3.9% | $23.88 | -1.9 | done | can't tell from luck |
| value_ev5 | 1708 | 39.9 | 41.0 | $-994.05 | -5.8% | $5.95 | -2.0 | done | losing for real |
| trend_filter | 1451 | 50.0 | 51.0 | $-999.41 | -6.9% | $0.59 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 2079 | 50.1 | 50.9 | $-1350.79 | -6.5% | $-350.79 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2514 | 49.4 | 50.4 | $-1412.16 | -5.6% | $-412.16 | -2.8 | done | losing for real |
| coinflip | 3560 | 50.3 | 50.3 | $-1516.79 | -4.3% | $-516.79 | -2.6 | done | losing for real |
| momentum_5m_0.00pct | 3560 | 51.2 | 51.7 | $-1660.55 | -4.7% | $-660.55 | -2.9 | done | losing for real |
| always_up | 3560 | 47.0 | 49.6 | $-3420.49 | -9.6% | $-2420.49 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5611 | 48.3 | 49.1 | $-3007.81 |
| ETH | 6125 | 48.3 | 48.5 | $-3690.96 |
| SOL | 6428 | 48.2 | 48.5 | $-3673.86 |
| XRP | 6452 | 48.3 | 48.5 | $-3575.03 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
