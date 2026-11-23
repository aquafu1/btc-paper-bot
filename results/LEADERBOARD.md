# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 1:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1220 windows, 33466 settled trades, 388 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 652 | 34.5 | 35.3 | $-443.45 | -6.8% | $556.55 | -1.3 | done | can't tell from luck |
| value_ev10 | 1599 | 38.8 | 39.2 | $-760.67 | -4.8% | $239.33 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3353 | 50.8 | 50.3 | $-1081.77 | -3.2% | $-81.77 | -1.9 | done | can't tell from luck |
| value_ev5 | 2417 | 40.5 | 41.1 | $-1175.89 | -4.9% | $-175.89 | -2.0 | done | losing for real |
| momentum_60m_0.30pct | 2809 | 49.6 | 49.4 | $-1266.88 | -4.5% | $-266.88 | -2.4 | done | losing for real |
| trend_filter | 1981 | 48.8 | 50.4 | $-1667.09 | -8.4% | $-667.09 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2809 | 50.4 | 51.1 | $-1679.58 | -6.0% | $-679.58 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3353 | 49.2 | 50.2 | $-2070.63 | -6.2% | $-1070.63 | -3.6 | done | losing for real |
| coinflip | 4831 | 50.0 | 50.1 | $-2226.96 | -4.6% | $-1226.96 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4831 | 50.3 | 51.4 | $-2917.50 | -6.0% | $-1917.50 | -4.3 | done | losing for real |
| always_up | 4831 | 47.8 | 49.3 | $-3541.50 | -7.3% | $-2541.50 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7767 | 48.1 | 48.9 | $-4352.26 |
| ETH | 8389 | 48.1 | 48.3 | $-4895.43 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
