# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 1:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 405 windows, 11110 settled trades, 28 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 201 | 36.3 | 36.5 | $-76.95 | -3.8% | $923.05 | -0.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 947 | 51.0 | 49.9 | $-178.51 | -1.9% | $821.49 | -0.6 | done | can't tell from luck |
| value_ev10 | 522 | 40.2 | 40.5 | $-204.41 | -3.9% | $795.59 | -0.7 | done | can't tell from luck |
| trend_filter | 626 | 50.2 | 50.6 | $-305.23 | -4.9% | $694.77 | -1.2 | done | can't tell from luck |
| value_ev5 | 784 | 42.0 | 42.2 | $-313.76 | -4.0% | $686.24 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1119 | 49.5 | 49.9 | $-474.86 | -4.2% | $525.14 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1119 | 50.5 | 51.9 | $-741.99 | -6.6% | $258.01 | -2.3 | done | losing for real |
| coinflip | 1615 | 50.2 | 50.9 | $-803.04 | -5.0% | $196.96 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 947 | 49.0 | 52.0 | $-897.29 | -9.5% | $102.71 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1615 | 49.8 | 51.6 | $-1088.83 | -6.7% | $-88.83 | -2.8 | done | losing for real |
| always_up | 1615 | 45.8 | 50.7 | $-2119.94 | -13.1% | $-1119.94 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2511 | 47.7 | 49.5 | $-1769.51 |
| ETH | 2794 | 47.9 | 48.9 | $-1769.86 |
| SOL | 2866 | 48.0 | 49.5 | $-2139.53 |
| XRP | 2939 | 48.9 | 49.3 | $-1525.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
