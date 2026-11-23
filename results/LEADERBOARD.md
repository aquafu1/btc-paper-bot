# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 5:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1237 windows, 33717 settled trades, 438 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 662 | 34.3 | 35.3 | $-494.16 | -7.5% | $505.84 | -1.5 | done | can't tell from luck |
| value_ev10 | 1614 | 38.7 | 39.2 | $-800.67 | -5.0% | $199.33 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3381 | 50.8 | 50.3 | $-1061.71 | -3.1% | $-61.71 | -1.8 | done | can't tell from luck |
| value_ev5 | 2439 | 40.4 | 41.1 | $-1267.46 | -5.2% | $-267.46 | -2.2 | done | losing for real |
| momentum_60m_0.30pct | 2827 | 49.5 | 49.4 | $-1279.75 | -4.5% | $-279.75 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 2827 | 50.5 | 51.1 | $-1677.47 | -5.9% | $-677.47 | -3.2 | done | losing for real |
| trend_filter | 1994 | 48.7 | 50.4 | $-1680.11 | -8.4% | $-680.11 | -3.9 | done | losing for real |
| momentum_15m_0.10pct | 3381 | 49.2 | 50.2 | $-2114.62 | -6.3% | $-1114.62 | -3.7 | done | losing for real |
| coinflip | 4864 | 50.0 | 50.1 | $-2212.65 | -4.5% | $-1212.65 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4864 | 50.2 | 51.4 | $-2981.28 | -6.1% | $-1981.28 | -4.4 | done | losing for real |
| always_up | 4864 | 47.8 | 49.3 | $-3587.90 | -7.4% | $-2587.90 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7886 | 48.0 | 48.9 | $-4567.33 |
| ETH | 8521 | 48.1 | 48.3 | $-5006.24 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
