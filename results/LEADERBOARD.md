# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 8:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1057 windows, 29269 settled trades, 22 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 545 | 34.7 | 35.1 | $-290.90 | -5.3% | $709.10 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2963 | 51.3 | 50.4 | $-739.81 | -2.5% | $260.19 | -1.4 | done | can't tell from luck |
| value_ev10 | 1354 | 37.7 | 39.2 | $-943.14 | -7.0% | $56.86 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 2488 | 49.6 | 49.6 | $-1192.80 | -4.8% | $-192.80 | -2.4 | done | losing for real |
| value_ev5 | 2055 | 39.6 | 41.0 | $-1357.00 | -6.6% | $-357.00 | -2.5 | done | losing for real |
| trend_filter | 1741 | 49.3 | 50.7 | $-1368.58 | -7.9% | $-368.58 | -3.4 | done | losing for real |
| reversal_60m_0.30pct | 2488 | 50.4 | 51.0 | $-1548.08 | -6.2% | $-548.08 | -3.2 | done | losing for real |
| coinflip | 4224 | 50.5 | 50.3 | $-1685.49 | -4.0% | $-685.49 | -2.6 | done | losing for real |
| momentum_15m_0.10pct | 2963 | 48.7 | 50.3 | $-2112.10 | -7.1% | $-1112.10 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4224 | 50.8 | 51.5 | $-2269.80 | -5.4% | $-1269.80 | -3.6 | done | losing for real |
| always_up | 4224 | 47.3 | 49.4 | $-3631.17 | -8.6% | $-2631.17 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6674 | 48.4 | 49.0 | $-3449.69 |
| ETH | 7239 | 48.1 | 48.5 | $-4570.82 |
| SOL | 7639 | 48.1 | 48.5 | $-4455.37 |
| XRP | 7717 | 48.2 | 48.3 | $-4662.98 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
