# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 26, 7:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1486 windows, 37265 settled trades, 337 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 756 | 34.3 | 35.4 | $-593.12 | -7.8% | $406.88 | -1.7 | done | can't tell from luck |
| value_ev10 | 1817 | 38.5 | 39.2 | $-975.06 | -5.4% | $24.94 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 3709 | 50.9 | 50.1 | $-1000.10 | -2.7% | $-0.10 | -1.6 | done | can't tell from luck |
| value_ev5 | 2739 | 40.4 | 41.1 | $-1436.86 | -5.2% | $-436.86 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 3118 | 51.0 | 51.0 | $-1487.24 | -4.8% | $-487.24 | -2.7 | done | losing for real |
| momentum_60m_0.30pct | 3118 | 49.0 | 49.2 | $-1646.03 | -5.3% | $-646.03 | -2.9 | done | losing for real |
| trend_filter | 2213 | 48.5 | 50.3 | $-1953.15 | -8.8% | $-953.15 | -4.2 | done | losing for real |
| momentum_15m_0.10pct | 3709 | 49.1 | 50.2 | $-2290.13 | -6.2% | $-1290.13 | -3.8 | done | losing for real |
| coinflip | 5362 | 49.9 | 50.0 | $-2392.88 | -4.5% | $-1392.88 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5362 | 50.1 | 51.3 | $-3411.62 | -6.4% | $-2411.62 | -4.8 | done | losing for real |
| always_up | 5362 | 48.0 | 49.2 | $-3560.14 | -6.6% | $-2560.14 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9618 | 48.0 | 48.7 | $-5351.10 |
| ETH | 10337 | 47.9 | 47.9 | $-5811.00 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
