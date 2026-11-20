# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 943 windows, 26102 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 481 | 34.9 | 34.9 | $-180.56 | -3.8% | $819.44 | -0.6 | done | can't tell from luck |
| value_ev10 | 1184 | 38.0 | 39.1 | $-698.57 | -5.9% | $301.43 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2667 | 51.1 | 50.6 | $-857.48 | -3.2% | $142.52 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2232 | 50.1 | 49.8 | $-961.05 | -4.3% | $38.95 | -2.0 | done | losing for real |
| trend_filter | 1551 | 49.9 | 51.0 | $-1100.13 | -7.1% | $-100.13 | -2.9 | done | losing for real |
| value_ev5 | 1796 | 39.7 | 41.0 | $-1138.64 | -6.3% | $-138.64 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2232 | 49.9 | 50.9 | $-1564.33 | -7.0% | $-564.33 | -3.4 | done | losing for real |
| coinflip | 3764 | 50.4 | 50.3 | $-1600.39 | -4.3% | $-600.39 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2667 | 48.9 | 50.3 | $-1793.49 | -6.7% | $-793.49 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 3764 | 50.9 | 51.6 | $-1985.29 | -5.3% | $-985.29 | -3.3 | done | losing for real |
| always_up | 3764 | 46.7 | 49.7 | $-3887.94 | -10.3% | $-2887.94 | -6.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5949 | 48.1 | 49.1 | $-3510.95 |
| ETH | 6493 | 48.1 | 48.6 | $-4147.50 |
| SOL | 6807 | 48.1 | 48.6 | $-4045.81 |
| XRP | 6853 | 48.3 | 48.5 | $-4063.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
