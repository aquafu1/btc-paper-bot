# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 11:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1167 windows, 32239 settled trades, 70 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 620 | 34.7 | 35.3 | $-375.55 | -6.1% | $624.45 | -1.1 | done | can't tell from luck |
| value_ev10 | 1524 | 38.5 | 39.2 | $-819.07 | -5.4% | $180.93 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3231 | 50.9 | 50.4 | $-1036.64 | -3.2% | $-36.64 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2721 | 49.7 | 49.4 | $-1134.61 | -4.2% | $-134.61 | -2.2 | done | losing for real |
| value_ev5 | 2304 | 40.3 | 41.1 | $-1232.93 | -5.4% | $-232.93 | -2.2 | done | losing for real |
| trend_filter | 1907 | 49.0 | 50.5 | $-1513.93 | -7.9% | $-513.93 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2721 | 50.3 | 51.1 | $-1719.62 | -6.3% | $-719.62 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3231 | 49.1 | 50.2 | $-1969.81 | -6.1% | $-969.81 | -3.5 | done | losing for real |
| coinflip | 4660 | 50.2 | 50.2 | $-1987.93 | -4.3% | $-987.93 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 4660 | 50.2 | 51.4 | $-2893.15 | -6.2% | $-1893.15 | -4.4 | done | losing for real |
| always_up | 4660 | 47.8 | 49.3 | $-3397.27 | -7.3% | $-2397.27 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7396 | 48.3 | 49.0 | $-3846.47 |
| ETH | 7997 | 48.2 | 48.4 | $-4650.86 |
| SOL | 8387 | 48.1 | 48.4 | $-4519.04 |
| XRP | 8459 | 48.1 | 48.2 | $-5064.15 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
