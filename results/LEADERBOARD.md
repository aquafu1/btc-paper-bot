# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 9:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1446 windows, 36731 settled trades, 405 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 740 | 34.5 | 35.3 | $-533.47 | -7.2% | $466.53 | -1.5 | done | can't tell from luck |
| value_ev10 | 1787 | 38.8 | 39.2 | $-816.32 | -4.6% | $183.68 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3666 | 50.9 | 50.1 | $-967.86 | -2.6% | $32.14 | -1.6 | done | can't tell from luck |
| value_ev5 | 2693 | 40.5 | 41.1 | $-1301.66 | -4.8% | $-301.66 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3076 | 49.2 | 49.2 | $-1519.80 | -4.9% | $-519.80 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3076 | 50.8 | 51.0 | $-1572.86 | -5.1% | $-572.86 | -2.9 | done | losing for real |
| trend_filter | 2178 | 48.5 | 50.3 | $-1897.44 | -8.7% | $-897.44 | -4.2 | done | losing for real |
| coinflip | 5283 | 50.0 | 50.0 | $-2257.50 | -4.3% | $-1257.50 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3666 | 49.1 | 50.2 | $-2294.76 | -6.3% | $-1294.76 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5283 | 50.1 | 51.3 | $-3337.38 | -6.3% | $-2337.38 | -4.7 | done | losing for real |
| always_up | 5283 | 48.0 | 49.2 | $-3563.99 | -6.7% | $-2563.99 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9361 | 48.1 | 48.7 | $-4933.67 |
| ETH | 10060 | 48.0 | 48.0 | $-5545.14 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
