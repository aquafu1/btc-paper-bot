# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 6:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1195 windows, 33012 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 645 | 34.7 | 35.3 | $-398.79 | -6.2% | $601.21 | -1.2 | done | can't tell from luck |
| value_ev10 | 1573 | 38.6 | 39.2 | $-822.09 | -5.2% | $177.91 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3308 | 50.8 | 50.3 | $-1079.77 | -3.3% | $-79.77 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2767 | 49.6 | 49.4 | $-1238.22 | -4.5% | $-238.22 | -2.3 | done | losing for real |
| value_ev5 | 2381 | 40.3 | 41.1 | $-1295.52 | -5.4% | $-295.52 | -2.3 | done | losing for real |
| trend_filter | 1947 | 48.7 | 50.5 | $-1652.80 | -8.5% | $-652.80 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2767 | 50.4 | 51.1 | $-1686.50 | -6.1% | $-686.50 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3308 | 49.2 | 50.3 | $-2042.85 | -6.2% | $-1042.85 | -3.6 | done | losing for real |
| coinflip | 4772 | 50.1 | 50.1 | $-2077.99 | -4.4% | $-1077.99 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 4772 | 50.2 | 51.4 | $-3007.26 | -6.3% | $-2007.26 | -4.5 | done | losing for real |
| always_up | 4772 | 47.8 | 49.3 | $-3539.84 | -7.4% | $-2539.84 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7580 | 48.1 | 48.9 | $-4269.57 |
| ETH | 8188 | 48.0 | 48.4 | $-5043.48 |
| SOL | 8593 | 48.2 | 48.4 | $-4413.60 |
| XRP | 8651 | 48.1 | 48.2 | $-5114.99 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
