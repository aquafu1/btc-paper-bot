# Paper trading leaderboard (FAKE money)

**Updated Fri Nov 20, 3:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 943 windows, 26115 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 481 | 34.9 | 34.9 | $-180.56 | -3.8% | $819.44 | -0.6 | done | can't tell from luck |
| value_ev10 | 1184 | 38.0 | 39.1 | $-698.57 | -5.9% | $301.43 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 2669 | 51.1 | 50.6 | $-877.48 | -3.3% | $122.52 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 2233 | 50.1 | 49.8 | $-971.05 | -4.3% | $28.95 | -2.1 | done | losing for real |
| trend_filter | 1552 | 49.9 | 51.0 | $-1088.47 | -7.0% | $-88.47 | -2.8 | done | losing for real |
| value_ev5 | 1796 | 39.7 | 41.0 | $-1138.64 | -6.3% | $-138.64 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 2233 | 49.9 | 50.9 | $-1552.49 | -7.0% | $-552.49 | -3.4 | done | losing for real |
| coinflip | 3766 | 50.4 | 50.3 | $-1598.55 | -4.2% | $-598.55 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2669 | 48.9 | 50.3 | $-1769.99 | -6.6% | $-769.99 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 3766 | 50.9 | 51.6 | $-1961.80 | -5.2% | $-961.80 | -3.3 | done | losing for real |
| always_up | 3766 | 46.8 | 49.7 | $-3864.45 | -10.3% | $-2864.45 | -6.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 5949 | 48.1 | 49.1 | $-3510.95 |
| ETH | 6493 | 48.1 | 48.6 | $-4147.50 |
| SOL | 6814 | 48.2 | 48.6 | $-4006.63 |
| XRP | 6859 | 48.3 | 48.5 | $-4036.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
