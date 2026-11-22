# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 21, 10:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1064 windows, 29444 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 548 | 34.7 | 35.1 | $-293.30 | -5.4% | $706.70 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 2980 | 51.2 | 50.4 | $-752.21 | -2.5% | $247.79 | -1.4 | done | can't tell from luck |
| value_ev10 | 1360 | 37.8 | 39.2 | $-910.20 | -6.7% | $89.80 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2505 | 49.8 | 49.6 | $-1084.93 | -4.3% | $-84.93 | -2.2 | done | losing for real |
| trend_filter | 1756 | 49.6 | 50.7 | $-1248.73 | -7.1% | $-248.73 | -3.1 | done | losing for real |
| value_ev5 | 2066 | 39.8 | 41.0 | $-1291.78 | -6.3% | $-291.78 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2505 | 50.2 | 51.0 | $-1632.04 | -6.5% | $-632.04 | -3.3 | done | losing for real |
| coinflip | 4248 | 50.4 | 50.3 | $-1724.13 | -4.1% | $-724.13 | -2.7 | done | losing for real |
| momentum_15m_0.10pct | 2980 | 48.8 | 50.3 | $-2096.21 | -7.0% | $-1096.21 | -3.9 | done | losing for real |
| momentum_5m_0.00pct | 4248 | 50.9 | 51.5 | $-2132.39 | -5.0% | $-1132.39 | -3.4 | done | losing for real |
| always_up | 4248 | 47.2 | 49.4 | $-3785.13 | -8.9% | $-2785.13 | -5.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 6720 | 48.4 | 49.0 | $-3448.68 |
| ETH | 7282 | 48.1 | 48.5 | $-4597.28 |
| SOL | 7682 | 48.1 | 48.5 | $-4426.16 |
| XRP | 7760 | 48.3 | 48.3 | $-4478.92 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
