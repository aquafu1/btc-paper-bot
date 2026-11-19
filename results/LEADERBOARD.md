# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 8:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 770 windows, 21232 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 401 | 33.2 | 34.9 | $-361.45 | -9.0% | $638.55 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2169 | 51.4 | 50.6 | $-582.29 | -2.7% | $417.71 | -1.3 | done | can't tell from luck |
| value_ev10 | 972 | 37.8 | 39.1 | $-674.62 | -6.9% | $325.38 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1795 | 49.7 | 49.6 | $-786.65 | -4.4% | $213.35 | -1.9 | done | can't tell from luck |
| value_ev5 | 1468 | 40.1 | 41.0 | $-854.74 | -5.8% | $145.26 | -1.9 | done | can't tell from luck |
| trend_filter | 1247 | 49.6 | 50.8 | $-855.43 | -6.9% | $144.57 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1795 | 50.3 | 51.2 | $-1136.18 | -6.3% | $-136.18 | -2.7 | done | losing for real |
| coinflip | 3072 | 50.3 | 50.3 | $-1249.71 | -4.1% | $-249.71 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2169 | 48.6 | 50.2 | $-1490.31 | -6.9% | $-490.31 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 3072 | 50.9 | 51.6 | $-1522.34 | -5.0% | $-522.34 | -2.8 | done | losing for real |
| always_up | 3072 | 47.2 | 49.6 | $-2735.64 | -8.9% | $-1735.64 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4819 | 48.2 | 49.1 | $-2842.94 |
| ETH | 5299 | 48.0 | 48.5 | $-3535.93 |
| SOL | 5527 | 48.1 | 48.5 | $-3203.62 |
| XRP | 5587 | 48.5 | 48.4 | $-2666.86 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
