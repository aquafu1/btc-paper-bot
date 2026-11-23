# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 22, 11:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1166 windows, 32227 settled trades, 45 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 620 | 34.7 | 35.3 | $-375.55 | -6.1% | $624.45 | -1.1 | done | can't tell from luck |
| value_ev10 | 1524 | 38.5 | 39.2 | $-819.07 | -5.4% | $180.93 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3231 | 50.9 | 50.4 | $-1036.64 | -3.2% | $-36.64 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2720 | 49.7 | 49.4 | $-1124.61 | -4.1% | $-124.61 | -2.1 | done | losing for real |
| value_ev5 | 2303 | 40.3 | 41.1 | $-1222.93 | -5.3% | $-222.93 | -2.2 | done | losing for real |
| trend_filter | 1907 | 49.0 | 50.5 | $-1513.93 | -7.9% | $-513.93 | -3.5 | done | losing for real |
| reversal_60m_0.30pct | 2720 | 50.3 | 51.1 | $-1726.89 | -6.3% | $-726.89 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3231 | 49.1 | 50.2 | $-1969.81 | -6.1% | $-969.81 | -3.5 | done | losing for real |
| coinflip | 4657 | 50.2 | 50.2 | $-1974.81 | -4.2% | $-974.81 | -2.9 | done | losing for real |
| momentum_5m_0.00pct | 4657 | 50.1 | 51.4 | $-2914.47 | -6.3% | $-1914.47 | -4.4 | done | losing for real |
| always_up | 4657 | 47.8 | 49.3 | $-3418.59 | -7.3% | $-2418.59 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7396 | 48.3 | 49.0 | $-3846.47 |
| ETH | 7992 | 48.1 | 48.4 | $-4652.67 |
| SOL | 8383 | 48.1 | 48.4 | $-4529.68 |
| XRP | 8456 | 48.0 | 48.2 | $-5068.49 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
