# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 11:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 735 windows, 20244 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 382 | 33.5 | 34.9 | $-322.66 | -8.4% | $677.34 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 2076 | 51.6 | 50.7 | $-468.01 | -2.3% | $531.99 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1702 | 50.1 | 49.6 | $-576.90 | -3.4% | $423.10 | -1.4 | done | can't tell from luck |
| value_ev10 | 925 | 38.1 | 39.1 | $-596.66 | -6.5% | $403.34 | -1.6 | done | can't tell from luck |
| value_ev5 | 1396 | 40.5 | 41.1 | $-721.72 | -5.2% | $278.28 | -1.6 | done | can't tell from luck |
| trend_filter | 1189 | 50.0 | 51.0 | $-730.04 | -6.1% | $269.96 | -2.2 | done | losing for real |
| coinflip | 2932 | 50.3 | 50.3 | $-1192.81 | -4.1% | $-192.81 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1702 | 49.9 | 51.2 | $-1219.69 | -7.2% | $-219.69 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2076 | 48.4 | 50.1 | $-1486.04 | -7.2% | $-486.04 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 2932 | 50.9 | 51.8 | $-1590.93 | -5.4% | $-590.93 | -3.0 | done | losing for real |
| always_up | 2932 | 47.1 | 49.6 | $-2649.07 | -9.0% | $-1649.07 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4587 | 48.1 | 49.1 | $-2871.33 |
| ETH | 5046 | 48.2 | 48.6 | $-3089.41 |
| SOL | 5271 | 48.2 | 48.7 | $-3012.30 |
| XRP | 5340 | 48.5 | 48.5 | $-2581.48 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
