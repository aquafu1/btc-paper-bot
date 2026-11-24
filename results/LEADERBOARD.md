# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 10:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1259 windows, 34035 settled trades, 417 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 665 | 34.1 | 35.3 | $-524.16 | -7.9% | $475.84 | -1.6 | done | can't tell from luck |
| value_ev10 | 1629 | 38.4 | 39.2 | $-908.07 | -5.6% | $91.93 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3412 | 50.7 | 50.3 | $-1167.75 | -3.4% | $-167.75 | -2.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 2857 | 49.6 | 49.4 | $-1241.92 | -4.3% | $-241.92 | -2.3 | done | losing for real |
| value_ev5 | 2462 | 40.3 | 41.1 | $-1357.52 | -5.5% | $-357.52 | -2.3 | done | losing for real |
| trend_filter | 2017 | 49.0 | 50.4 | $-1610.06 | -8.0% | $-610.06 | -3.7 | done | losing for real |
| reversal_60m_0.30pct | 2857 | 50.4 | 51.1 | $-1751.69 | -6.1% | $-751.69 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3412 | 49.3 | 50.2 | $-2051.34 | -6.0% | $-1051.34 | -3.6 | done | losing for real |
| coinflip | 4908 | 50.1 | 50.1 | $-2179.36 | -4.4% | $-1179.36 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4908 | 50.4 | 51.4 | $-2848.73 | -5.8% | $-1848.73 | -4.2 | done | losing for real |
| always_up | 4908 | 47.9 | 49.4 | $-3611.48 | -7.4% | $-2611.48 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 8044 | 48.1 | 48.9 | $-4670.84 |
| ETH | 8681 | 48.2 | 48.3 | $-4997.01 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
