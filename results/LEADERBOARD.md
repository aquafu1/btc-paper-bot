# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 5:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1191 windows, 32901 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 641 | 34.9 | 35.3 | $-358.79 | -5.6% | $641.21 | -1.1 | done | can't tell from luck |
| value_ev10 | 1566 | 38.7 | 39.2 | $-774.19 | -4.9% | $225.81 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3293 | 50.9 | 50.3 | $-1023.73 | -3.1% | $-23.73 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2763 | 49.6 | 49.4 | $-1212.74 | -4.4% | $-212.74 | -2.3 | done | losing for real |
| value_ev5 | 2371 | 40.4 | 41.1 | $-1262.33 | -5.3% | $-262.33 | -2.2 | done | losing for real |
| trend_filter | 1943 | 48.8 | 50.5 | $-1627.32 | -8.4% | $-627.32 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2763 | 50.4 | 51.1 | $-1701.96 | -6.2% | $-701.96 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3293 | 49.1 | 50.2 | $-2065.75 | -6.3% | $-1065.75 | -3.6 | done | losing for real |
| coinflip | 4756 | 50.1 | 50.2 | $-2090.69 | -4.4% | $-1090.69 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4756 | 50.1 | 51.4 | $-3054.88 | -6.4% | $-2054.88 | -4.6 | done | losing for real |
| always_up | 4756 | 47.9 | 49.3 | $-3455.06 | -7.3% | $-2455.06 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7553 | 48.2 | 48.9 | $-4175.49 |
| ETH | 8160 | 48.0 | 48.4 | $-5018.39 |
| SOL | 8560 | 48.2 | 48.4 | $-4351.22 |
| XRP | 8628 | 48.1 | 48.2 | $-5082.33 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
