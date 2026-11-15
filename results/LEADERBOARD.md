# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 2:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 411 windows, 11263 settled trades, 64 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 202 | 36.1 | 36.5 | $-86.95 | -4.3% | $913.05 | -0.5 | done | can't tell from luck |
| value_ev10 | 527 | 40.2 | 40.5 | $-213.81 | -4.1% | $786.19 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 963 | 50.9 | 50.0 | $-224.67 | -2.3% | $775.33 | -0.7 | done | can't tell from luck |
| value_ev5 | 794 | 42.1 | 42.2 | $-314.02 | -4.0% | $685.98 | -1.0 | done | can't tell from luck |
| trend_filter | 638 | 49.8 | 50.7 | $-353.07 | -5.5% | $646.93 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1134 | 49.2 | 49.9 | $-553.69 | -4.9% | $446.31 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1134 | 50.8 | 51.9 | $-686.19 | -6.1% | $313.81 | -2.1 | done | losing for real |
| coinflip | 1636 | 50.2 | 50.9 | $-799.04 | -4.9% | $200.96 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 963 | 49.1 | 51.9 | $-874.83 | -9.1% | $125.17 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 1636 | 49.7 | 51.6 | $-1151.68 | -7.0% | $-151.68 | -2.9 | done | losing for real |
| always_up | 1636 | 45.8 | 50.6 | $-2128.55 | -13.0% | $-1128.55 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2546 | 47.6 | 49.5 | $-1842.64 |
| ETH | 2831 | 47.9 | 49.0 | $-1770.98 |
| SOL | 2914 | 47.9 | 49.5 | $-2245.11 |
| XRP | 2972 | 48.9 | 49.3 | $-1527.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
