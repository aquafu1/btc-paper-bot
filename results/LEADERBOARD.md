# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 9:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1110 windows, 30727 settled trades, 29 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 586 | 34.3 | 35.1 | $-390.56 | -6.7% | $609.44 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 3099 | 51.2 | 50.4 | $-776.74 | -2.5% | $223.26 | -1.4 | done | can't tell from luck |
| value_ev10 | 1432 | 37.8 | 39.1 | $-980.15 | -6.8% | $19.85 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2607 | 49.8 | 49.4 | $-1081.63 | -4.1% | $-81.63 | -2.1 | done | losing for real |
| trend_filter | 1819 | 49.3 | 50.4 | $-1365.33 | -7.5% | $-365.33 | -3.3 | done | losing for real |
| value_ev5 | 2170 | 39.8 | 41.0 | $-1375.13 | -6.3% | $-375.13 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 2607 | 50.2 | 51.1 | $-1696.36 | -6.5% | $-696.36 | -3.4 | done | losing for real |
| coinflip | 4436 | 50.5 | 50.2 | $-1698.74 | -3.8% | $-698.74 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 3099 | 48.8 | 50.2 | $-2137.63 | -6.9% | $-1137.63 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4436 | 50.7 | 51.4 | $-2390.04 | -5.4% | $-1390.04 | -3.7 | done | losing for real |
| always_up | 4436 | 47.5 | 49.3 | $-3569.32 | -8.0% | $-2569.32 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7033 | 48.4 | 49.0 | $-3514.49 |
| ETH | 7613 | 48.1 | 48.4 | $-4647.25 |
| SOL | 8000 | 48.0 | 48.4 | $-4533.07 |
| XRP | 8081 | 48.1 | 48.2 | $-4766.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
