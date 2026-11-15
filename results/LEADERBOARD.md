# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 2:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 410 windows, 11255 settled trades, 42 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 202 | 36.1 | 36.5 | $-86.95 | -4.3% | $913.05 | -0.5 | done | can't tell from luck |
| value_ev10 | 527 | 40.2 | 40.5 | $-213.81 | -4.1% | $786.19 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 962 | 50.9 | 50.0 | $-214.67 | -2.2% | $785.33 | -0.7 | done | can't tell from luck |
| value_ev5 | 794 | 42.1 | 42.2 | $-314.02 | -4.0% | $685.98 | -1.0 | done | can't tell from luck |
| trend_filter | 637 | 49.9 | 50.7 | $-343.07 | -5.4% | $656.93 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1133 | 49.2 | 49.9 | $-543.69 | -4.8% | $456.31 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1133 | 50.8 | 51.9 | $-695.13 | -6.1% | $304.87 | -2.2 | done | losing for real |
| coinflip | 1635 | 50.2 | 50.9 | $-807.98 | -4.9% | $192.02 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 962 | 49.1 | 51.9 | $-883.77 | -9.2% | $116.23 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1635 | 49.7 | 51.6 | $-1141.68 | -7.0% | $-141.68 | -2.9 | done | losing for real |
| always_up | 1635 | 45.7 | 50.6 | $-2137.48 | -13.1% | $-1137.48 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2546 | 47.6 | 49.5 | $-1842.64 |
| ETH | 2823 | 47.9 | 49.0 | $-1766.72 |
| SOL | 2914 | 47.9 | 49.5 | $-2245.11 |
| XRP | 2972 | 48.9 | 49.3 | $-1527.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
