# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 5:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 372 windows, 10082 settled trades, 76 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 192 | 37.5 | 36.6 | $-14.22 | -0.7% | $985.78 | -0.1 | Sat 9:00 PM | too few trades (192/200) |
| value_ev10 | 491 | 40.5 | 40.5 | $-146.39 | -3.0% | $853.61 | -0.5 | done | can't tell from luck |
| value_ev5 | 723 | 41.9 | 42.1 | $-286.26 | -4.0% | $713.74 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 835 | 49.8 | 49.8 | $-364.01 | -4.4% | $635.99 | -1.3 | done | can't tell from luck |
| trend_filter | 558 | 49.3 | 50.6 | $-380.47 | -6.8% | $619.53 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1004 | 51.6 | 52.1 | $-495.60 | -4.9% | $504.40 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1004 | 48.4 | 49.7 | $-618.77 | -6.2% | $381.23 | -1.9 | done | can't tell from luck |
| reversal_60m_0.30pct | 835 | 50.2 | 52.0 | $-619.09 | -7.4% | $380.91 | -2.2 | done | losing for real |
| coinflip | 1480 | 49.8 | 50.8 | $-830.88 | -5.6% | $169.12 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1480 | 49.8 | 51.6 | $-1020.16 | -6.9% | $-20.16 | -2.7 | done | losing for real |
| always_up | 1480 | 45.6 | 50.7 | $-2012.52 | -13.6% | $-1012.52 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2269 | 47.3 | 49.4 | $-1808.58 |
| ETH | 2534 | 47.7 | 48.9 | $-1790.52 |
| SOL | 2612 | 48.0 | 49.5 | $-1882.36 |
| XRP | 2667 | 48.8 | 49.1 | $-1306.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
